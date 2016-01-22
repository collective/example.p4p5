from plone import api
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class TasksView(BrowserView):
    """
    """

    template = ViewPageTemplateFile("tasks.pt")

    def __call__(self):
        """
        """
        tasks = api.content.find(portal_type='Task')
        results = {
            'done': 0,
            'inprogress': 0,
        }
        for brain in tasks:
            if 'In progress' in brain.getObject().status:
                results['inprogress'] += 1
            else:
                results['done'] += 1
        self.results = results

        return self.template()
