from datetime import datetime,timedelta
from ApiCallService import make_api_call
from DataBaseService import DataBaseService

class BaseService:

    def __init__(self):
        self.db_service = DataBaseService()

    def get_mined_blocks(self,ip):
        blocks  = make_api_call()
        mined_blocks = len(blocks)

        self.db_service.save_log(ip,1,mined_blocks)
        return mined_blocks

    def get_av_time(self,ip):
        blocks = make_api_call()
        av_time = 0.0

        for i in range(len(blocks) - 1):
            block1_time = datetime.strptime(blocks[i]['time'], '%Y-%m-%d %H:%M:%S').timestamp()
            block2_time = datetime.strptime(blocks[i + 1]['time'], '%Y-%m-%d %H:%M:%S').timestamp()
            av_time += (block1_time - block2_time)

        av_time /= len(blocks)
        av_time /= 60

        self.db_service.save_log(ip,2,av_time)
        return round(av_time,2)

    def get_tx_count(self,ip):
        blocks = make_api_call()
        tx_amount = 0

        for block in blocks:
            tx_amount += block['transaction_count']

        self.db_service.save_log(ip, 3, tx_amount)
        return tx_amount

    def get_fee_count(self,ip):
        blocks = make_api_call()
        fees_amount = 0

        for block in blocks:
            fees_amount += block['fee_total']

        self.db_service.save_log(ip, 4, fees_amount)
        return fees_amount

    def get_input_count(self,ip):
        blocks = make_api_call()
        input_amount = 0

        for block in blocks:
            input_amount += block['input_count']

        self.db_service.save_log(ip, 5, input_amount)
        return input_amount

    def get_output_count(self,ip):
        blocks = make_api_call()
        output_amount = 0

        for block in blocks:
            output_amount += block['output_count']

        self.db_service.save_log(ip, 6, output_amount)
        return output_amount
