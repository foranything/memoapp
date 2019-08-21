import axios from "axios";

export function getMemo() {
  // return axios.get("https://jsonplaceholder.typicode.com/posts/" + postId);
  return axios.get("http://127.0.0.1:8000/memos/all/");
}
//
// export function getComments(postId) {
//   return axios.get(
//     `https://jsonplaceholder.typicode.com/posts/${postId}/comments`
//   );
// }
