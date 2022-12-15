class FetchBase {
  constructor() {}

  async fetch(url, method = "GET") {
    const res = await fetch(url, {
      method: method,
    });
    const data = await res.json();

    return data;
  }
}
export const fetchBase = new FetchBase();
