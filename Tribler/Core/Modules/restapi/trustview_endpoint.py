from __future__ import absolute_import

from twisted.web import http, resource

import Tribler.Core.Utilities.json_util as json


class TrustViewEndpoint(resource.Resource):
    """
    This endpoint is responsible for handing requests for trustchain data.
    """

    def __init__(self, session):
        resource.Resource.__init__(self)

        child_handler_dict = {
            b"test": TrustViewTestEndpoint,
        }

        for path, child_cls in child_handler_dict.items():
            self.putChild(path, child_cls(session))


class TrustViewBaseEndpoint(resource.Resource):
    """
    This class represents the base class of the trustchain community.
    """

    def __init__(self, session):
        resource.Resource.__init__(self)
        self.session = session


class TrustViewTestEndpoint(TrustViewBaseEndpoint):
    """
    This class handles requests regarding the trustchain community information.
    """

    def render_GET(self, request):
        from random import randint, random # Put here because to be deleted
        import networkx as nx
        gr = nx.watts_strogatz_graph(10, 4, 0.5)
        pos = {}
        for n in gr.nodes():
            pos[n] = (random(), random())
        grs = nx.node_link_data(gr)

        return json.twisted_dumps({'test_data'  : "Hello World {}".format(randint(0, 100)),
                                   'test_graph' : grs,
                                   'positions'  : pos})