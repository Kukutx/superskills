---
description: bug-diagnosis ranks causes by evidence and verifies before cache-clearing or reinstalling
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

急，Next.js 项目本地 `npm run dev` 一切正常，昨天部署到服务器（Docker，`npm run build && npm start`）之后 /orders 页面直接 500，其他页面都好的。服务器日志：

```
TypeError: Cannot read properties of undefined (reading 'map')
    at OrdersPage (/app/.next/server/pages/orders.js:1:2381)
```

orders 页面的代码：

```js
export async function getServerSideProps() {
  const res = await fetch(`${process.env.API_BASE_URL}/orders`);
  const data = await res.json();
  return { props: { orders: data.items } };
}

export default function OrdersPage({ orders }) {
  return <ul>{orders.map(o => <li key={o.id}>{o.title}</li>)}</ul>;
}
```

本地 API_BASE_URL 是写在 .env.local 里的。昨天还顺手把 next 从 13 升到了 14。到底咋回事，怎么修？
