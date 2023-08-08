from graphviz import Digraph
from sql_models import Base

# Create a Graphviz Digraph object
graph = Digraph('ERD', format='png')

# Set the nodesep attribute to control the minimum distance between nodes
graph.attr(nodesep='2')  # inches

# Iterate over the SQLAlchemy models
for table in Base.metadata.tables.values():
    table_name = table.name

    # Create the label for the table node
    label = f'<<TABLE><TR><TD><FONT POINT-SIZE="40" FACE="DejaVu Sans">▦ <b>{table_name}</b></FONT></TD></TR>'

    # sorted columns, first primary keys, then foreign keys, then other attributes
    sorted_columns = sorted(list(table.columns), key=lambda x: (not x.primary_key, not x.foreign_keys))
    # Add the primary key columns to the table node
    for column in sorted_columns:
        symbol = "(⚷)" if column.primary_key else "⚷⚷" if column.foreign_keys else "◻"
        color = "#F9C23C" if column.primary_key else "gray" if column.foreign_keys else "black"
        label += f'<TR><TD ALIGN="LEFT"><FONT POINT-SIZE="30" FACE="DejaVu Sans" COLOR="{color}">{symbol} {column.name}</FONT></TD></TR>'

    label += '</TABLE>>'

    # Add the table as a node in the graph with the label
    graph.node(table_name, label=label, shape='record')

    # Iterate over the foreign key relationships
    for foreign_key in table.foreign_keys:
        referenced_table = foreign_key.column.table.name
        foreign_key_column = foreign_key.column.name
        referenced_column = foreign_key.column.table.primary_key.columns.values()[0].name

        # Add the foreign key relationship as an edge in the graph with the foreign key and referenced key labels
        graph.edge(table_name, referenced_table, label=f'{foreign_key_column}', fontsize="30", fontname="Helvetica")

# Render the graph and save it as an image file
graph.render('Rockbuster_ERD', view=True)


