from PySide2.QtGui import QValidator
from PySide2.QtCore import Signal

class RuleExpressionValidator(QValidator):
    validation_status_changed = Signal(QValidator.State, str)

    def __init__(self, sim_expression_parser, is_formula=True, parent=None):
        super().__init__(parent)
        self.parser = sim_expression_parser
        self.is_formula = is_formula

    def validate(self, text, pos):
        valid, message, _ = self.parser.validate_expression(text, self.is_formula)
        state = QValidator.Acceptable if valid else QValidator.Intermediate

        self.validation_status_changed.emit(state, message)
        return (state, text, pos)