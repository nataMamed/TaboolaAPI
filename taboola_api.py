import requests
import pandas as pd
from datetime import datetime, timedelta



class TaboolaAPI:

    def __init__(self, client_id, client_secret, account_id, token=''):
        self.client_id = client_id
        self.client_secret = client_secret
        self.account_id = account_id
        self.access_token = self.make_access_token(token)

    def make_access_token(self, token):
        
        if token:
            return token
        else:
            url = "https://backstage.taboola.com/backstage/oauth/token"

            payload = f"client_id={self.client_id}&client_secret={self.client_secret}&grant_type=client_credentials"
            headers = {"content-type": "application/x-www-form-urlencoded"}

            resp = requests.post(url, data=payload, headers=headers).json()

        return resp['access_token']


    def fetch_campaigns(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        url = "https://backstage.taboola.com/backstage/api/1.0/mobills-br-sc/campaigns/"
        
        response = requests.get(url, headers = headers)
        campaigns = response.json()['results']


        # campaign_list = []

        # for campaign in campaigns:
        #     campaign_list.append({'id': campaign['id'], 'name': campaign['name']})
        
        return campaigns
    

    def fetch_campaigns_data(self, start_date, end_date):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }


        url = f"https://backstage.taboola.com/backstage/api/1.0/{self.account_id}/reports/campaign-summary/dimensions/campaign_day_breakdown?start_date={start_date}&end_date={end_date}"

        response = requests.get(url, headers=headers).json()['results']

        return response


if __name__=='__main__':
    cli_id = ''
    cli_sec = ''
    acc_id = ''
    end_date  = datetime.now().date() - timedelta(days=1)
    end_date = end_date.strftime('%Y-%m-%d')

    start_date = '2022-10-07'

    api = TaboolaAPI(client_id=cli_id, client_secret=cli_sec, account_id=acc_id)
    result = api.fetch_campaigns_data(start_date=start_date, end_date=end_date)