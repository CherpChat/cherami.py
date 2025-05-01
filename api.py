import httpx

class API:
    def __init__(self, token, base_url='https://cherami.chat'):
        self._token = token
        self.base_url = base_url

    def notifications(self):
        return self._get('notifications')

    def chats(self):
        return self._get('chats')

    def chat(self, uuid, search=None):
        if search:
            return self._get(f'chats/{uuid}/search', {'q': search})
        else:
            return self._get(f'chats/{uuid}')
    
    # Format: { title: "text", description: "text", hide_latest: true, icon: "🫵" }  
    def edit_chat(self, uuid, json):
        return self._patch(f'chats/{uuid}', json)
    
    def delete_chat(self, uuid):
        return self._delete(f'chats/{uuid}')
    
    # Format: { content: "text", color: "#000000", visibility: "ic", chat_id: 12345 }    
    def create_message(self, json):
        return self._post('messages')
    
    def message(self, id):
        return self._get(f'messages/{id}')
    
    # Format: { content: "text", color: "#000000", visibility: "ic" }
    def edit_message(self, id, json):
        return self._patch(f'messages/{id}', json)

    def _header(self):
        return {'Authorization': f'Bearer {self._token}'}

    def _endpoint(self, endpoint):
        return f'{self.base_url}/{endpoint if endpoint.endswith('.json') else endpoint + '.json'}'
    
    def _get(self, endpoint, params={}):
        result = httpx.get(self._endpoint(endpoint),
                            headers=self._header(),
                            params=params)
        return result.json()
    
    def _post(self, endpoint, json={}):
        result = httpx.post(self._endpoint(endpoint),
                            headers=self._header(),
                            json=json)
        return result.json()

    def _patch(self, endpoint, json={}):
        result = httpx.patch(self._endpoint(endpoint),
                            headers=self._header(),
                            json=json)
        return result.json()

    def _delete(self, endpoint):
        result = httpx.delete(self._endpoint(endpoint),
                            headers=self._header())
        return result.json()