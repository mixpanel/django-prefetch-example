import logging
import re
import traceback


# https://markusholtermann.eu/2016/01/syntax-highlighting-for-djangos-sql-query-logging/
class SQLFormatter(logging.Formatter):
    def format(self, record):
        # Check if Pygments is available for coloring
        try:
            import pygments
            from pygments.lexers import SqlLexer
            from pygments.formatters import TerminalTrueColorFormatter
        except ImportError:
            pygments = None

        # Check if sqlparse is available for indentation
        try:
            import sqlparse
        except ImportError:
            sqlparse = None
        # Remove leading and trailing whitespaces
        sql = record.sql.strip()

        if sqlparse:
            # Indent the SQL query
            sql = sqlparse.format(sql, reindent=True)

        if pygments:
            # Highlight the SQL query
            sql = pygments.highlight(
                sql, SqlLexer(), TerminalTrueColorFormatter(style="default")
            )

        
        record.statement = sql
        return super(SQLFormatter, self).format(record)
