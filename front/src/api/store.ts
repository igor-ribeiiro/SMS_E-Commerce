import axios from "axios";

import {IStoreItem, isBuiltIn, needField, checkStore} from "./types";

export async function fetchStore(): Promise<IStoreItem[]> {
    const resp = await axios.get("https://vtexhackathon-api.herokuapp.com/shelf")
    const body = resp.data;

    if (isBuiltIn("object")(body)) {
        if (needField(body, "result", checkStore)) {
            return body.result;
        }
    }

    return [];
}
