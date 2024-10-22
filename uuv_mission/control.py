#Code that implements the PD controller.
class PDController:
    def __init__(self, proportional_gain=0.15, derivative_gain=0.6):
        self.proportional_gain = proportional_gain
        self.derivative_gain = derivative_gain
        self.previous_error = 0

    def compute_control_action(self, error):
        derivative = error - self.previous_error
        control_action = self.proportional_gain * error + self.derivative_gain * derivative
        self.previous_error = error
        return control_action