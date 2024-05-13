import pandas
from functools import partial
from IPython.display import display

display_options = {
    'wide': 'display.max_columns',
    'long': 'display.max_rows',
    'uncut': 'display.max_colwidth',
}

def patch():
    def _validate(opts):
        invalid = list(set(opts) - set(display_options))
        if invalid:
            raise ValueError(
                f'{invalid} not in valid display options: {list(display_options)}'
            )

    def _display(self, *opts):
        _validate(opts)
        options = sum([[display_options[opt], None] for opt in opts], [])
        with pandas.option_context(*options):
            display(self)
    
    pandas.core.generic.NDFrame.display = _display
    pandas.core.generic.NDFrame.long = partial(_display, 'long')
    pandas.core.generic.NDFrame.wide = partial(_display, 'wide')
    pandas.core.generic.NDFrame.uncut = partial(_display, 'uncut')
    pandas.core.generic.NDFrame.full = partial(_display, *display_options)

__all__ = ['patch']
