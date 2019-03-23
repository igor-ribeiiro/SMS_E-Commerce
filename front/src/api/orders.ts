import { IOrder, IOrders } from "./types";

const MOCK_ORDERS: IOrder[] = [
    {
      id: 0,
      enviado: true,
      timestamp: 123123131,
      name: "João",
      telefone: "+1 12 121321",
      endereco: "Rua H8B, 215E",
      items: [{
        quantidade: 121,
        descricao: "Coca-Cola"
      }, {
        quantidade: 1232,
        descricao: "Skol"
      }]
    },
    {
      id: 1,
      enviado: false,
      timestamp: 1231242312,
      name: "Pedro",
      telefone: "+1 12 121321",
      endereco: "Rua H8A, 121F",
      items: [{
        quantidade: 121,
        descricao: "Coca-Cola"
      }, {
        quantidade: 1232,
        descricao: "Skol"
      }]
    },
    {
      id: 20,
      enviado: false,
      timestamp: 123123131,
      name: "João",
      telefone: "+1 12 121321",
      items: [{
        quantidade: 121,
        descricao: "Coca-Cola"
      }, {
        quantidade: 1232,
        descricao: "Skol"
      }]
    },
    {
      id: 10,
      enviado: true,
      timestamp: 1231242312,
      name: "Pedro",
      telefone: "+1 12 121321",
      items: [{
        quantidade: 121,
        descricao: "Coca-Cola"
      }, {
        quantidade: 1232,
        descricao: "Skol"
      }]
    },
];

export async function fetchOrders(): Promise<IOrders> {
    let orders: IOrder[] = MOCK_ORDERS;

    orders = orders.sort((o1, o2) => o2.timestamp - o1.timestamp);

    let resp: IOrders = { delivery: [], stored: [] }

    for (const order of orders) {
        if (order.endereco) {
            resp.delivery.push(order);
        } else {
            resp.stored.push(order);
        }
    }

    return Promise.resolve(resp);
}


export async function finishOrder(order: IOrder) {
    if (order.enviado) return Promise.resolve();

    for (const or of MOCK_ORDERS) {
      if (or.id === order.id) or.enviado = true;
    }
}
