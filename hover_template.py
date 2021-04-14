'''
    Provides the templates for the tooltips.
'''


def map_base_hover_template():
    '''
        Sets the template for the hover tooltips on the neighborhoods.

        The label is simply the name of the neighborhood in font 'Oswald'.

        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template
    value_style = 'style = "font-family : Oswald;"'
    hover = f'<span {value_style}> ' + '%{location}</span>' \
            '<extra></extra>'
    return hover


def map_marker_hover_template(name):
    '''
        Sets the template for the hover tooltips on the markers.

        The label is simply the name of the walking path in font 'Oswald'.

        Args:
            name: The name to display
        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template
    value_style = 'style = "font-family : Oswald;"'
    hover = f'<span {value_style}> ' + name +'</span>' \
            '<extra></extra>'
    return hover