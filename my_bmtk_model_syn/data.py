from bmtk.utils.cell_vars import CellVarsFile
from bmtk.analyzer.cell_vars import _get_cell_report

def get_variable_report(config_file=None, report_file=None, report_name=None, variable=None, gid=None):
    """Returns variable reports for specified gids
    Function will return the report for a specific cell's variable.
    """
    if report_file is None:
        report_name, report_file = _get_cell_report(config_file, report_name)

    var_report = CellVarsFile(report_file)
    time_steps = var_report.time_trace

    return var_report.data(gid=gid, var_name=variable), time_steps