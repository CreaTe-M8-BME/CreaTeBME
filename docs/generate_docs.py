from pydoc_markdown import PydocMarkdown
from pydoc_markdown.interfaces import Context
from pydoc_markdown.contrib.loaders.python import PythonLoader
from pydoc_markdown.contrib.renderers.markdown import MarkdownRenderer

session = PydocMarkdown()

assert isinstance(session.loaders[0], PythonLoader)
session.loaders[0].search_path = ['src/CreaTeBME']
assert isinstance(session.renderer, MarkdownRenderer)
modules = session.load_modules()
session.process(modules)
session.renderer.render_toc = True
session.renderer.render_page_title = 'Test'
for module in modules:
    with open(f'docs/modules/{module.name}.md', 'w') as f:
        session.renderer.render_single_page(f, [module], module.name)

