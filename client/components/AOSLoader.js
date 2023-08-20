import { useEffect } from "react";
import { useRouter } from "next/router";

const AOSLoader = () => {
  const router = useRouter();
  useEffect(() => {
    const handleRouteChange = () => {
      if (window.AOS) {
        window.AOS.refresh();
        // If refresh doesn't work, try destroying and reinitializing
        window.AOS.init({
          once: false, // whether animation should happen only once - while scrolling down
        });
      }
    };

    router.events.on("routeChangeComplete", handleRouteChange);

    return () => {
      router.events.off("routeChangeComplete", handleRouteChange);
    };
  }, []);

  return null;
};

export default AOSLoader;
