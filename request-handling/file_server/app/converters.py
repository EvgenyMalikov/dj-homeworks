from datetime import datetime


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format_ = '%Y-%m-%d'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, self.format_)

    def to_url(self, value: datetime) -> str:
        return value.strftime(self.format_)
