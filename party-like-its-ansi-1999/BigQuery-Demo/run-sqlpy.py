from google.cloud import bigquery
from sqlpy import Queries


class Cursor:
    """Define a object which implements methods
    of the DB 2.0 API, holds results and other
    requiried utilities.
    """
    def __init__(self, clinet):
        self._client = clinet
        self._results = None

    def execute(self, query, args=None):
        query_job = self._client.query(query)
        self._results = query_job.result()

    def fetchall(self):
        return self._results


def query_stackoverflow():
    client = bigquery.Client()  # init bigquery client
    sql = Queries('queries.sql')  # init SQLpy Query object with query file
    cur = Cursor(client)  # init cursor object

    # execute the query against BigQuery
    # use the name defined in queries.sql
    # as the function name, passing cursour
    results, _ = sql.PYTHON_QUESTION_VIEWS(cur)

    for row in results:
        print("- {:<50} : {} [{} views]".format(row.title[:50],
                                                row.url,
                                                row.view_count))


if __name__ == '__main__':
    query_stackoverflow()
