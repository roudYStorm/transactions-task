import sys

sys.path.append('./modules')
sys.path.append('./utils')

from task import runTransactionQuestions, runSorts, runTransactionsInfo

runTransactionQuestions()
runSorts()
runTransactionsInfo()