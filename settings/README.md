### The classic settings path has been changed.

I set module loading via Enum `Environment` from module 
`settings.environment.settings` and the classic `settings.py` 
was completely removed. More precisely, it was divided into 
two levels `Environment`.


In my opinion, this way the `settings` structure is cleaner.

You don't need to worry about it. 
Just interact with the settings module you need from 
`settings.environment.*.py` where * is one of the Enum options 
`settings.environment.settings.Environment`.