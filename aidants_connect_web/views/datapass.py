import logging

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest

from aidants_connect_web.models import Organisation

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


def receiver(request):
    try:
        if request.META["HTTP_AUTHORIZATION"] != settings.DATAPASS_KEY:
            log.info("403: Bad authorization header for datapass call")
            return HttpResponseForbidden()
    except KeyError:
        log.info("403: No authorization header for datapass call")
        return HttpResponseForbidden()

    if request.method != "POST":
        return HttpResponse("This is a POST only route")

    parameters = {
        "data_pass_id": request.POST.get("data_pass_id"),
        "organization_name": request.POST.get("organization_name"),
        "organization_siret": request.POST.get("organization_siret"),
        "organization_address": request.POST.get("organization_address"),
    }
    for parameter, value in parameters.items():
        if not value:
            error_message = f"400 Bad request: There is no {parameter} @ datapass"
            log.info(error_message)
            return HttpResponseBadRequest()
        if (
            parameter in ["organization_siret", "data_pass_id"]
            and not value.isnumeric()
        ):
            error_message = f"400 Bad request: {parameter} is NaN @ datapass"
            log.info(error_message)
            return HttpResponseBadRequest()

    try:
        this_organisation = Organisation.objects.create(
            name=parameters["organization_name"],
            siret=parameters["organization_siret"],
            address=parameters["organization_address"],
        )
    except ValueError as e:
        log.info(f"{e} @ datapass")
        return HttpResponseBadRequest()

    send_mail(
        subject="Une nouvelle structure",
        message=f"""
            la structure {this_organisation.name} vient
            d'être validée pour avoir des accès à Aidants Connect.
            ###
            Vous pouvez consulter la demande sur :
            https://datapass.api.gouv.fr/aidantsconnect/{parameters["data_pass_id"]}
        """,
        from_email=settings.DATAPASS_FROM_EMAIL,
        recipient_list=[settings.DATAPASS_TO_EMAIL],
        fail_silently=False,
    )

    return HttpResponse(status=202)
