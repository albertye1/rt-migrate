from pathlib import Path 

from transpire.resources import Deployment, Ingress, Secret, Service

name = "rt"
auto_sync = True 

def objects():
    yield Service(
        name = "service"
        # fill rest later..
    )
    yield Deployment(
        name = "deployment"
        # fill rest later..
    )
    yield Ingress(
        name = "virtual-host-ingress"
        # fill rest later..
    )
    yield Secret(
        name = "keycloak-secret"
        # fill rest later..
    )
