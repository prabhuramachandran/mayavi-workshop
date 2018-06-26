import glob
import os


DOIT_CONFIG = {'default_tasks': ['pdf', 'notebook']}


def task_pdf():
    for fname in ['01_intro.tex']:
        name = os.path.splitext(fname)[0]
        yield {
            'name': name,
            'actions': ['pdflatex %s' % fname]*2,
            'file_dep': ['common.tex', fname],
            'targets': [name + '.pdf'],
            'clean': True,
        }


def task_notebook():
    for fname in glob.glob('*.ipyml'):
        name = os.path.splitext(fname)[0]
        dest = name + '.ipynb'
        yield {
            'name': name,
            'actions': [
                'ipyaml --no-output {src} {dest}'.format(src=fname, dest=dest)
            ],
            'file_dep': ['common.tex', fname],
            'targets': [dest],
            'clean': True,
        }


def task_cleanup():
    globs = '*.aux *.log *.nav *.out *.snm *.toc *.vrb'.split()
    files = [f for g in globs for f in glob.glob(g)]

    def _remove(targets):
        for t in targets:
            os.remove(t)

    return {'actions': [_remove], 'targets': files}
