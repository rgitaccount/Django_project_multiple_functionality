from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ("GoodReads", "GoodReads"),
        ("NYT", "NYT"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            "media_type",
        ]

    def parse_data(self):
        if self.data['media_type'] == "GoodReads":
            goodreads_parser = parser.parser_func()
            for data in goodreads_parser:
                models.GoodReads.objects.create(**data)
        elif self.data['media_type'] == "NYT":
            nyt_parser = parser.parser_func_nyt()
            for data in nyt_parser:
                models.NytBooks.objects.create(**data)
