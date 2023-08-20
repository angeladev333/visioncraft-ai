import React, { useState } from "react";
import { redirect } from "next/navigation";

export default function ImageForm() {
  const [submissionStatus, setSubmissionStatus] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);

    const options = {
      method: "POST",
      body: formData,
    };

    const response = await fetch("/api/upload_image/", options);
    const result = await response.json();
    // check if error
    if (result.error) {
      alert(result.error);
      setSubmissionStatus("error");
    } else {
      setSubmissionStatus("success");
      // redirect to result["ipfs_url"] value in result
      //   alert(result["ipfs_url"]);
      window.location.href = result["ipfs_url"];
    }
  };
  return (
    <div className="flex items-center justify-center text-center h-full min-h-[calc(100vh-150px)]">
      <form onSubmit={handleSubmit} data-aos="fade-up">
        <div className="mb-6">
          <label
            htmlFor="whatcreate"
            className="block mb-2 text-sm font-medium text-gray-900"
          >
            What do you want to create?
          </label>
          <input
            type="text"
            name="whatcreate"
            id="whatcreate"
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
            placeholder="A Mini PC"
            required
          />
        </div>
        <div className="mb-6">
          <label
            htmlFor="materials"
            className="block mb-2 text-sm font-medium text-gray-900"
          >
            What materials do you have?
          </label>
          <input
            type="text"
            name="materials"
            id="materials"
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
            placeholder="Power Adapter, Motherboard, ..."
            required
          />
        </div>
        <div className="mb-6">
          <label
            htmlFor="budget"
            className="block mb-2 text-sm font-medium text-gray-900"
          >
            What is your budget?
          </label>
          <input
            type="number"
            name="budget"
            id="budget"
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
            placeholder="2000"
            required
          />
        </div>

        <label
          className="block mb-2 text-sm font-medium text-gray-900"
          htmlFor="user_avatar"
        >
          Upload Image of Hardware Parts.
        </label>
        <input
          name="image"
          className="mb-6 block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50"
          aria-describedby="user_avatar_help"
          id="user_avatar"
          type="file"
        />

        <button
          type="submit"
          className="rounded-full text-white bg-blue-500 hover:bg-blue-700 focus:ring-4 focus:ring-blue-300 font-medium w-48 text-sm px-5 py-2.5 mr-2 mb-2"
        >
          Submit
        </button>

        {submissionStatus === "success" && (
          <div className="mt-4 text-green-500">
            Submitted successfully! Redirecting...
          </div>
        )}
      </form>
    </div>
  );
}
