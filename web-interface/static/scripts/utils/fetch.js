class FetchBase {
  constructor() {}

  async fetch(url, method = "GET", body) {
    try {
      const res = await fetch(url, {
        method: method,
        body: body ? body : null,
      });
      const data = await res.json();

      return data;
    } catch (e) {
      console.log(e);
    }
  }
}
export const fetchBase = new FetchBase();
