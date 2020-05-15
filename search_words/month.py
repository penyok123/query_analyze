q = {'filter': {'bool': {'should': [{'bool': {
    'must': [{'nested': {'path': 'special', 'query': {'bool': {'must': [{'term': {'special.id': 801}}]}}}}]}}],
    'must': [{'term': {'is_online': True}}]}}}

q['filter']['bool']['should'].append({'terms': {'first_classify_ids': [1]}})
q['filter']['bool']['should'].append({'terms': {'second_classify_ids': [1]}})
q['filter']['bool']['should'].append({'terms': {'tags_v3': [1]}})
q['filter']['bool']['should']['minimum_should_match'] = 1

print(q)
