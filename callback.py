'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle no clicks on the map
    style = {
            'visibility': 'hidden',
            'border': '1px solid black',
            'padding': '10px'}
    title, mode, theme = None, None, None
    return title, mode, theme, style


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the map base
    return title, mode, theme, style


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the markers
    customdata = figure['data'][curve]['customdata'][0]

    title_str = customdata['nom_projet'][point]
    mode_str = customdata['mode_implantation'][point]
    theme_str = customdata['objectif_thematique'][point]
    markercolor_str = figure['data'][curve]['marker']['color']
    
    title = html.Span(title_str, style={'color': markercolor_str})
    mode = html.Span(mode_str, style={'font-weight' : 'bold'})

    if theme_str:
        theme_str_list = theme_str.split('\n')   
        theme = [html.P('Thématique:')]
        theme.append(html.Ul([
            html.Li(theme_str_list[i], style={}) for i in range(0, len(theme_str_list))
            ]))
    else:
        theme = None
    
    style = {
        'visibility': 'visible',
        'border': '1px solid black',
        'padding': '10px',
        }

    return title, mode, theme, style
