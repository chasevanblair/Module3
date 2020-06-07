from format_output import average_scores as avg


def test_average(self):
    with mock.patch('builtins.input', side_effect=[85,90,95]):
        assert avg.average() == 90