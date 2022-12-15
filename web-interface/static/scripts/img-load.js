const getImg = async () => {
  const response = await fetch("/images", {
    method: "GET",
  });

  const data = await response.json();
  return data;
};

getImg();

const renderImg = async () => {
  const data = await getImg();

  const ul = document.querySelector("#img");

  console.log(data);

  data.forEach((img) => {
    const li = document.createElement("li");
    li.classList.add("js-img-item");
    const imgElement = document.createElement("img");
    imgElement.src = img.url;
    imgElement.classList.add("js-img");
    li.appendChild(imgElement);
    ul.appendChild(li);
  });
};

renderImg();
