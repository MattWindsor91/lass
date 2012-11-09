"""
Template tags for the `grid` system.

"""

from django import template

from grid.models import GridBlock, Grid

register = template.Library()


@register.inclusion_tag('grid/generic.html', takes_context=True)
def grid_block(context, block_id):
    """
    Renders the grid block of the given ID.

    :param block_id: the ID (name or primary key) of the block
    :type block_id: string, integer or `GridBlock`
    :rtype: a template tag node

    """
    # Effectively pass the entire existing context with the
    # difference that 'box' is set to the block ID.
    # This is required for embedded views to work properly, just
    # returning a context of {'box': GridBlock.get(block_id)} causes
    # embedded views to break.
    context['box'] = GridBlock.get(block_id)
    return context


@register.inclusion_tag('grid/grid.html', takes_context=True)
def grid(context, grid_id):
    """
    Renders the grid of the given ID.

    This block simply outputs the blocks instanced in the grid in
    sequence; you will generally want to ensure that your grid CSS
    automatically breaks the grid stream into rows and columns.

    :param grid_id: the ID (name or primary key) of the grid
    :type grid_id: string, integer or `GridBlock`
    :rtype: a template tag node

    """
    # As grid_block and for the same reasons, but obviously with
    # 'grid' instead of 'box'.
    context['grid'] = Grid.get(grid_id)
    return context
