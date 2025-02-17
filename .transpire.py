from pathlib import Path
from transpire.resources import Deployment, Ingress, Secret, Service
from transpire.utils import get_image_tag

name = "rt"
auto_sync = True 

def objects():
    svc = Service(
        name = "rt-service",
        selector = {
            'app': name,
        },
        port_on_pod = 80,
        port_on_svc = 80,
        # fill rest later..
    )
    dep = Deployment(
        name = "rt-deployment",
        image = get_image_tag(name),
        # fill rest later..
    )
    ing = Ingress.from_service(
        svc = svc,
        host = "//rt.ocf.berkeley.edu",
        path_prefix = "/",
    )
    sec = Secret(
        name = "keycloak-secret",
        string_data = {
            # not sure how to translate the yaml for this one...
            'secret': 'placeholder',
            'encryption_key': 'placeholder',
        }
        # fill rest later..
    )

    # build all objects and yield.
    yield svc.build()
    yield dep.build()
    yield ing.build()
    yield sec.build()
