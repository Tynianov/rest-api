Statictics of bitcoin network for last 24 hour

Built with AWS Lambda + AWS API Gateway

Blockhain info got from: https://blockchair.com/

API returns information about bitcoin network for last 24 hours:

•	Mined blocks

•	Average time between blocks

•	Amount of transactions

•	Fees amount

•	Input amount

•	Output amount

Request for mined blocks: https://he61mw8pc6.execute-api.us-east-1.amazonaws.com/statistics/get-mined-blocks

Request for average time between blocks: https://he61mw8pc6.execute-api.us-east-1.amazonaws.com/statistics/get-average-time

Request for transactions amount: https://he61mw8pc6.execute-api.us-east-1.amazonaws.com/statistics/get-tx-amount

Request for fees amount: https://he61mw8pc6.execute-api.us-east-1.amazonaws.com/statistics/get-fee-amount

Request for input amount: https://he61mw8pc6.execute-api.us-east-1.amazonaws.com/statistics/get-input-count

Request for output amount: https://he61mw8pc6.execute-api.us-east-1.amazonaws.com/statistics/get-output-count

