from .start import register_start_handlers
from .help import register_help_handlers

def register_handlers(bot):
    register_start_handlers(bot)
    register_help_handlers(bot)
    # ... другие обработчики

