export default function ImageForm() {
    const handleSubmit = async (event) => {
        event.preventDefault();

        const formData = new FormData(event.target);

        const options = {
            method: "POST",
            body: formData,
        };

        const response = await fetch("/api/upload_image/", options);
        // alert(await response.text());
        const result = await response.json();
        // check if error
        if (result.error) {
            alert(result.error);
        } else{
            
        }
    };
    return (
        <div className="flex items-center justify-center text-center h-full min-h-[calc(100vh-150px)]">
            <form onSubmit={handleSubmit}>
                <div className="mb-6">
                    <label for="whatcreate" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">What do you want to create?</label>
                    <input type="text" name="whatcreate" id="whatcreate" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="A Mini PC" required />
                </div>
                <div className="mb-6">
                    <label for="materials" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">What materials do you have?</label>
                    <input type="text" name="materials" id="materials" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Power Adapter, Motherboard, ..." required />
                </div>
                <div className="mb-6">
                    <label for="budget" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">What is your budget?</label>
                    <input type="number" name="budget" id="budget" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="2000" required />
                </div>

                <label
                    className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    htmlFor="user_avatar"
                >
                    Upload file
                </label>
                <input
                    name="image"
                    className="mb-6 block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
                    aria-describedby="user_avatar_help"
                    id="user_avatar"
                    type="file"
                />
                {/* <div
          className="mt-1 text-sm text-gray-500 dark:text-gray-300"
          id="user_avatar_help"
        >
          A profile picture is useful to confirm your are logged into your
          account
        </div> */}
                <button
                    type="submit"
                    className="rounded-full text-white bg-blue-500 hover:bg-blue-700 focus:ring-4 focus:ring-blue-300 font-medium w-48 text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
                >
                    Submit
                </button>
            </form>
        </div>
    );
}
