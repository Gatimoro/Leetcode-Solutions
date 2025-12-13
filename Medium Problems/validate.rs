impl Solution { 
    pub fn validate_coupons(
        code: Vec<String>,
        business_line: Vec<String>,
        is_active: Vec<bool>,
    ) -> Vec<String> {
        let business_line_order = ["electronics", "grocery", "pharmacy", "restaurant"];

        let mut valid_coupons: Vec<(usize, String)> = code
            .into_iter()
            .zip(business_line.into_iter())
            .zip(is_active.into_iter())
            .filter_map(|((code, category), active)| {
                if active && !code.is_empty() && code.chars().all(|c| c.is_alphanumeric() || c == '_') {
                    business_line_order
                        .iter()
                        .position(|&cat| cat == category)
                        .map(|order| (order, code))
                } else {
                    None
                }
            })
            .collect();

        valid_coupons.sort_by(|(order_a, code_a), (order_b, code_b)| {
            order_a.cmp(order_b).then(code_a.cmp(code_b))
        });

        valid_coupons.into_iter().map(|(_, code)| code).collect()
    }
}
