type Row = {
  service: string;
  country: string;
  price: string;
};

export function PriceTable({ rows }: { rows: Row[] }) {
  return (
    <table>
      <tbody>
        {rows.map((row) => (
          <tr key={`${row.service}-${row.country}`}>
            <td>{row.service}</td>
            <td>{row.country}</td>
            <td>{row.price}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
