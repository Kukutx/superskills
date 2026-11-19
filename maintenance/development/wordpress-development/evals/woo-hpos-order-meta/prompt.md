---
description: wordpress-development fixes order meta code for HPOS instead of switching storage back
runs: 2
max_turns: 6
allowed_tools: [Skill]
---

我们给客户写的一个小插件：订单完成时去物流公司建单，把运单号存起来，后台订单列表多一列显示运单号。

```php
add_action( 'woocommerce_order_status_completed', function ( $order_id ) {
    update_post_meta( $order_id, '_tracking_number', my_create_shipment( $order_id ) );
} );

add_filter( 'manage_edit-shop_order_columns', function ( $columns ) {
    $columns['tracking'] = 'Tracking';
    return $columns;
} );

add_action( 'manage_shop_order_posts_custom_column', function ( $column, $post_id ) {
    if ( 'tracking' === $column ) {
        echo get_post_meta( $post_id, '_tracking_number', true );
    }
}, 10, 2 );
```

客户这周在 WooCommerce 设置里把订单存储切到了“高性能订单存储”，之后这一列不见了，新订单的运单号也读不到。最快的办法是不是把存储切回去？
