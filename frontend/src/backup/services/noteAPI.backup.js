import axios from "axios";

export function getMemo() {
  return axios.get("http://127.0.0.1:8000/api/v1/memos/");
}

// export function postNote() {
//   return axios.post("http://127.0.0.1:8000/api/v1/memos/",{
//
//   });
// }
//
// export function getComments(postId) {
//   return axios.get(
//     `https://jsonplaceholder.typicode.com/posts/${postId}/comments`
//   );
// }
