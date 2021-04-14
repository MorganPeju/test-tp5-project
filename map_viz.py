'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover

def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # TODO : Draw the map base
    fig.add_traces(go.Choroplethmapbox(
        geojson=montreal_data, 
        locations=locations, 
        featureidkey='properties.NOM',
        z=z_vals,
        colorscale=colorscale, 
        showscale=False,
        marker_line_color='white',
        hovertemplate=hover.map_base_hover_template(),
        )
    )
    
    return fig

def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # TODO : Add the scatter markers to the map base
    type_site_intervention = list(street_df['properties.TYPE_SITE_INTERVENTION'].drop_duplicates())
    
    for site_i in range (0, len(type_site_intervention)):
        type_site_location = street_df[street_df['properties.TYPE_SITE_INTERVENTION'] == type_site_intervention[site_i]]
        fig.add_trace(go.Scattermapbox(
            lon=type_site_location['properties.LONGITUDE'],
            lat=type_site_location['properties.LATITUDE'],
            name=type_site_intervention[site_i],
            mode='markers',
            marker=go.scattermapbox.Marker(
                color=px.colors.qualitative.Plotly[site_i],
                size=10,
                opacity=0.4
            ),
            hovertemplate=hover.map_marker_hover_template(type_site_intervention[site_i]),
            customdata = [{
                'nom_projet': type_site_location['properties.NOM_PROJET'].values,
                'mode_implantation' : type_site_location['properties.MODE_IMPLANTATION'].values,
                'objectif_thematique' : type_site_location['properties.OBJECTIF_THEMATIQUE'].values,
             }]
            )
        )

    return fig
