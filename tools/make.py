from invoke import task

source = 'sphinx'
dest = 'build'
docs = 'docs'


@task
def build(ctx, cmd='help'):
    """Pass cmd to sphinx-build"""
    ctx.run('sphinx-build -M {} {} {}'.format(cmd, source, dest))


@task
def clean(ctx):
    """Clean build directory"""
    ctx.run('sphinx-build -M clean {} {}'.format(source, dest))


@task
def run(ctx):
    """Run test server that points to docs directory"""
    ctx.run('python -m http.server --directory {}'.format(docs))


@task
def update(ctx):
    """Transfer built files from build directory to docs directory"""
    exclude = '--exclude=.buildinfo --exclude=objects.inv'
    options = '-avz --delete-excluded {}'.format(exclude)
    ctx.run('rsync {} {}/html/ {}'.format(options, dest, docs))


@task
def html(ctx):
    """Rebuild html files and start test server"""
    clean(ctx)
    build(ctx, 'html')
    update(ctx)
    run(ctx)
