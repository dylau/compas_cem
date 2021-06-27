from compas.utilities import iterable_like


__all__ = ["form_plotter_proxy"]


def form_plotter_proxy(**kwargs):
    """
    """
    from compas_cem.plotters import FormPlotter

    # unpack kwargs
    form = kwargs["form"]
    filepath = kwargs["filepath"]

    edge_key = kwargs.get("edge_key")
    edge_width = kwargs.get("edge_width", 1.0)

    node_key = kwargs.get("node_key")
    node_radius = kwargs.get("node_radius", 0.1)
    node_edgewidth = kwargs.get("node_edgewidth", 1.0)

    load_scale = kwargs.get("load_scale", 1.0)
    load_gap = kwargs.get("load_gap", 0.1)

    reaction_scale = kwargs.get("reaction_scale", 1.0)
    reaction_gap = kwargs.get("reaction_gap", 0.1)

    segment = kwargs.get("segment", [])
    segment_color = kwargs.get("segment_color") or iterable_like(segment, [], (50, 50, 50))
    segment_width = kwargs.get("segment_width") or iterable_like(segment, [], 0.5)
    segment_ls = kwargs.get("segment_ls") or iterable_like(segment, [], "--")

    fig_width = kwargs.get("fig_width", 16)
    fig_height = kwargs.get("fig_height", 9)
    fig_dpi = kwargs.get("fig_dpi", 100)
    fig_tight = kwargs.get("fig_tight", False)

    # plot
    plotter = FormPlotter(form, figsize=(fig_width, fig_height), dpi=fig_dpi)

    plotter.draw_edges(keys=edge_key, width=edge_width)
    plotter.draw_nodes(keys=node_key, radius=node_radius, edgewidth=node_edgewidth)
    plotter.draw_loads(scale=load_scale, gap=load_gap)
    plotter.draw_residuals(scale=reaction_scale, gap=reaction_gap)

    for seg, ls, color, width in zip(segment, segment_ls, segment_color, segment_width):
        plotter.draw_segments([seg], color, width, ls)

    plotter.save(filepath, tight=fig_tight)