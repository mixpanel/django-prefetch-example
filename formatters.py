import logging
import re
import traceback


def get_line():
    try:
        last_line = [line for line in traceback.format_stack() if "myproject" in line][-3]
        pattern = r"\"(.*?)\", line (\d+),.*?\n(.*?)\n"
        match = re.search(pattern, last_line)
        if match:
            file_path, line_number, next_line = match.groups()
            return f"{file_path}:{line_number}\n {next_line}"
    except:
        return ""


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

        # Set the record's statement to the formatted query
        statement = sql
        line_executing_code = get_line()
        if line_executing_code:
            statement = f"{line_executing_code}\n{sql}"
        record.statement = statement
        return super(SQLFormatter, self).format(record)
