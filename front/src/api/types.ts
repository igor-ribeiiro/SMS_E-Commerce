export interface IStoreItem {
    quantidade: number;
    descricao: string;
    preco: number;
}

export function needField<T extends object, K extends string | symbol, V>(x: T, field: K, val: (a: any) => a is V): x is T & Record<K, V>  {
    const fieldValue = (x as any)[field]
    return fieldValue !== undefined && val(fieldValue);
}

function optionalField<T extends object, K extends string | symbol, V>(x: T, field: K, val: (a: any) => a is V): x is T & Record<K, V | undefined> {
    const fieldValue = (x as any)[field];
    return fieldValue === undefined || val(fieldValue);
}

type BuiltIns<K>
    = K extends "number" ? number
    : K extends "string" ? string
    : K extends "object" ? object
    : K extends "boolean" ? boolean
    : undefined;

export function isBuiltIn<K extends string>(builtin: K): (x: any) => x is BuiltIns<K> {
    return (x: any): x is BuiltIns<K> => typeof x === builtin;
}

function checkStoreItem(a: object): a is IStoreItem {
    return needField(a, "quantidade", isBuiltIn("number"))
        && needField(a, "descricao", isBuiltIn("string"))
        && needField(a, "preco", isBuiltIn("number"))
        && a.preco > 0;
}

export function checkStore(as: any): as is IStoreItem[] {
    return Array.isArray(as) && as.every(checkStoreItem)
}

export interface IOrders {
    delivery: IOrder[],
    stored: IOrder[]
}

export interface IOrder {
    id: number,
    enviado: boolean,
    timestamp: number,
    name: string,
    telefone: string,
    endereco?: string,
    items: IOrderItem[]
}

export interface IOrderItem {
    quantidade: number;
    descricao: string;
}

function checkOrderItem(x: any): x is IOrderItem {
    return needField(x, "quantidade", isBuiltIn("number"))
        && needField(x, "descricao", isBuiltIn("string"));
}

function checkOrder(x: object): x is IOrder {
    return needField(x, "id", isBuiltIn("number"))
        && needField(x, "enviado", isBuiltIn("boolean"))
        && needField(x, "timestamp", isBuiltIn("number"))
        && needField(x, "name", isBuiltIn("string"))
        && needField(x, "telefone", isBuiltIn("string"))
        && optionalField(x, "endereco", isBuiltIn("string"))
        && needField(x, "items", (is: any): is is IOrderItem[] => Array.isArray(is) && is.every(checkOrderItem))
}

export function checkOrders(x: any): x is IOrder[] {
    return Array.isArray(x) && x.every(checkOrder);
}
