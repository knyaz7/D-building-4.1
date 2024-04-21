import { createBrowserRouter } from "react-router-dom"
import { TransactionHistory } from "@/features/transactionsHistory"
import { MainPage } from "@/pages/main"
import { Services } from "@/pages/services"

export const router = createBrowserRouter([
  { path: "/", element: <MainPage /> },
  { path: "/transactionshistory", element: <TransactionHistory /> },
  { path: "/services/:entityName/:id", element: <Services /> },
])
