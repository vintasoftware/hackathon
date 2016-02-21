# coding: utf-8

from requests.auth import HTTPBasicAuth

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)
from tapioca.exceptions import (
    ResponseProcessException, ClientError, ServerError)

from tapioca_concept_insights.resource_mapping import RESOURCE_MAPPING


class ConceptInsightsClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    resource_mapping = RESOURCE_MAPPING

    def get_api_root(self, api_params):
        return 'https://gateway.watsonplatform.net/concept-insights/api/v2'

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(ConceptInsightsClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)
        params['auth'] = HTTPBasicAuth(
            api_params.get('user'), api_params.get('password'))

        params['headers']['Content-Type'] = 'text/html'
        return params

    def get_iterator_list(self, response_data):
        return response_data


ConceptInsights = generate_wrapper_from_adapter(ConceptInsightsClientAdapter)
