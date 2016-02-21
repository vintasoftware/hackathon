
from tapioca_concept_insights import ConceptInsights
from tapioca.exceptions import TapiocaException


ACCOUNT_ID = 'wikipedia'
GRAPH = 'en-latest'


cli = ConceptInsights(user='c1bb3173-3264-4222-b108-c74a17b8ea3a', password='8qdul5gM5N5K')


def extract_tags(text):
	try:
		response = cli.annotate_text(account_id=ACCOUNT_ID, graph=GRAPH).post(data=text)
	except TapiocaException as e:
		print(e.client().data)

	return list(set([c.concept.label().data for c in response.annotations]))


