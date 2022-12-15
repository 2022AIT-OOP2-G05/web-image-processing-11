const form = document.getElementById("form");
const fileInput = document.getElementById("file-input");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  postImg();
});

const postImg = async () => {
  const formData = new FormData(form);

  formData.append("file", fileInput.files[0]);
  console.log(formData);
  const response = await fetch("/upload", {
    method: "POST",
    body: formData,
  });

  const data = await response.json();
  console.log(data);
};

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

  const ul = document.querySelector("ul");

  console.log(data);

  data.forEach((img) => {
    const li = document.createElement("li");
    const imgElement = document.createElement("img");
    imgElement.src = img.url;
    li.appendChild(imgElement);
    ul.appendChild(li);
  });
};

renderImg();
