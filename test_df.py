from df import process_data
df = process_data('foo.csv')
assert df.columns.to_list() == ['id', 'customer_name', 'total_purchases']