


def test_format_multiple(self):
    expected_output = 'Salt Lake City, United States'
    actual_output = format_city_country('salt lake city', 'united states')
    self.assertEqual(actual_output, expected_output)